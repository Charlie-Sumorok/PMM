import { BrowserWindow } from 'electron';
import path from 'path';

const showPreferences = async () => {
	const win = new BrowserWindow({
		title: 'Preferences',
		show: false,

		width: 600,
		height: 450,

		webPreferences: {
			nodeIntegration: true,
		},
	});

	win.on('ready-to-show', () => {
		win.show();
	});

	await win.loadFile('../../../../views/preferences.html');

	return win;
};

export { showPreferences };
