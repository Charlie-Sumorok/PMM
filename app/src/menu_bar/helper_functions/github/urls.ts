export const form_query = (query_map: Map<string, string>) => {
	const query: string[] = [];
	for (const key of query_map.keys()) {
		query.push(`${key}=${query_map.get(key)}`);
	}
	return query.join('&');
};
