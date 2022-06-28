import { execSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

// Default value `youtube-dl-aas` if no args provided via CLI.
const appName = process.argv[2] || 'youtube-dl-aas';

const main = process.argv[3] || 'main.py';

const requirementsList = process.argv[4] || 'requirements';

const generateExecutable = (process.argv[5] || 'true') === 'true';

const startDir = process.cwd()
const webGuiDir = path.join(startDir, 'web-gui');
process.chdir(webGuiDir);

// install web gui dependencies
console.log('installing npm dependencies');
execSync('npm install');

// generate web gui static files
console.log('generating web gui static files');
execSync('npx ng build --configuration=production');

const serverDir = path.join(startDir, 'server')
process.chdir(serverDir);

// move ng build files inside server folder
const staticFilesDir = path.join(webGuiDir, 'dist', 'web-gui');
const serverStaticFilesDir = path.join(serverDir, 'resources');

const moveToServerDir = (fileName, serverSubdir) => {
    const webGuiFile = path.join(staticFilesDir, fileName);
    const serverDir = path.join(serverStaticFilesDir, serverSubdir);
    const serverFile = path.join(serverDir, fileName);
    console.log(`move ${webGuiFile} in ${serverFile}`);
    if (!fs.existsSync(serverDir)) {
        fs.mkdirSync(serverDir, { recursive: true });
    }
    fs.renameSync(webGuiFile, serverFile);
}

// move index.html to server/src/resources/templates
moveToServerDir('index.html', 'templates');

fs.readdirSync(staticFilesDir).forEach(fileName => {
    // move files to server/src/resources/home
    moveToServerDir(fileName, 'home');
});

// install server release requirements
console.log('installing server release requirements');
if (requirementsList.split(',').length == 0) {
    console.error('input requirements file has not been specified');
} else {
    requirementsList.split(',').forEach(requirement => {
        execSync(`python3 -m pip install -r ${requirement}.txt`);
    });
}

const addDataSeparator = process.platform === 'win32' ? ';' : ':';

function addFolderResource(folder) {
    return `--add-data "${folder}${addDataSeparator}${folder}"`;
}

function addFileResource(folder, fileName) {
    return `--add-data "${folder}/${fileName}${addDataSeparator}${folder}"`;
}

// create ${appName} executable in server/dist
if (generateExecutable) {
    const generateExecutableCmd = [
        `pyinstaller --onefile --name ${appName}`,
        addFolderResource('resources/templates'),
        addFolderResource('resources/home'),
        addFileResource('resources', 'icon.png'),
        `src/${main}`
    ].join(' ');
    console.log(`creating ${appName} executable in server/dist`);
    execSync(generateExecutableCmd);
} else {
    console.log('skipping executable creation via pyinstaller');
}
