export const form_query = (query_map: Map<string, string>) => {
	let query: string[] = [];
	query_map.forEach((key: string) => {
		query.push(`${key}=${query_map.get(key)}`);
	});
	return query.join('&');
};
