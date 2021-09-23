import Store from 'electron-store';

export const storage = new Store({
	defaults: {
		package_managers: {
			apm: false,
			npm: false,
			brew: false,
			pip: false,
		},
	},
});

