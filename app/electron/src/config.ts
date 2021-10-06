import Store from 'electron-store';

export const storage = new Store({
	defaults: {
		packageManagers: {
			apm: false,
			npm: false,
			brew: false,
			pip: false,
		},
	},
});
