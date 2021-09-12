import { app, shell } from 'electron';
import { aboutMenuItem, appMenu, is, platform } from 'electron-util';
import path from 'node:path';

import { storage } from '../config';
import { showPreferences } from '../preferences';
import {
	GitHubIssue,
	GitHubRepo,
	gitHubIssueFromTemplate,
	gitHubRepo_MenuBar_Item,
} from './helper_functions/github';
import { SubMenu } from './helper_functions/menus';

const main_repo: GitHubRepo = {
	owner: 'Charlie-Sumorok',
	name: 'ppm',
};

const feature_request = new GitHubIssue({
	labels: 'enhancement',
	template: 'feature-request.md',
	title: 'Add+Feature',
});

const bug_report = new GitHubIssue({
	labels: 'bug',
	template: 'bug-report.md',
	title: 'Bug+Report',
});

const helpSubmenu: SubMenu = [
	gitHubRepo_MenuBar_Item({
		label: 'Website',
		repo: main_repo,
	}),
	gitHubRepo_MenuBar_Item({
		label: 'Source Code',
		repo: main_repo,
	}),
	{
		type: 'separator',
	},
	gitHubIssueFromTemplate({
		label: 'Report an Issue …',
		repo: main_repo,
		issue: bug_report,
	}),
	gitHubIssueFromTemplate({
		label: 'Feature Request',
		repo: main_repo,
		issue: feature_request,
	}),
];

if (!is.macos) {
	helpSubmenu.push(
		{
			type: 'separator',
		},
		aboutMenuItem({
			icon: path.join(__dirname, '../../icons', 'icon.png'),
			text: 'Created by {Your Name}',
		})
	);
}

const debugSubmenu: SubMenu = [
	{
		label: 'Show Settings',
		click() {
			storage.openInEditor();
		},
	},
	{
		label: 'Show App Data',
		click() {
			void shell.openPath(app.getPath('userData'));
		},
	},
	{
		type: 'separator',
	},
	{
		label: 'Delete Settings',
		click() {
			storage.clear();
			app.relaunch();
			app.quit();
		},
	},
	{
		label: 'Delete App Data',
		async click() {
			await shell.trashItem(app.getPath('userData'));
			app.relaunch();
			app.quit();
		},
	},
];

const macosTemplate: SubMenu = [
	appMenu([
		{
			label: 'Preferences…',
			accelerator: 'Command+,',
			click() {
				void showPreferences();
			},
		},
	]),
	{
		role: 'fileMenu',
		submenu: [
			{
				label: 'Custom',
			},
			{
				type: 'separator',
			},
			{
				role: 'close',
			},
		],
	},
	{
		role: 'editMenu',
	},
	{
		role: 'viewMenu',
	},
	{
		role: 'windowMenu',
	},
	{
		role: 'help',
		submenu: helpSubmenu,
	},
];

// Linux and Windows
const otherTemplate: SubMenu = [
	{
		role: 'fileMenu',
		submenu: [
			{
				label: 'Custom',
			},
			{
				type: 'separator',
			},
			{
				label: 'Settings',
				accelerator: 'Control+,',
				click() {
					void showPreferences();
				},
			},
			{
				type: 'separator',
			},
			{
				role: 'quit',
			},
		],
	},
	{
		role: 'editMenu',
	},
	{
		role: 'viewMenu',
	},
	{
		role: 'help',
		submenu: helpSubmenu,
	},
];

const template = platform({
	macos: macosTemplate,
	default: otherTemplate,
});

if (is.development) {
	template.push({
		label: 'Debug',
		submenu: debugSubmenu,
	});
}

export { template };
