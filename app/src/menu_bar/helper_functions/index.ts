export const form_query = (query_map: Map<string, string>) => {
	let query = '';
	query_map.forEach((key: string) => {
		query += `${key}=${query_map.get(key)}`;
	});
	return query;
};

export * as github from './github';
export * as menus from './menus';
