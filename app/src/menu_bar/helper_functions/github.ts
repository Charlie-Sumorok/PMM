import { openUrlMenuItem } from 'electron-util';

import { form_query } from '.';

export class GitHubRepo {
	owner = '';
	name = '';
	url? = '';
	constructor(repo: GitHubRepo) {
		this.owner = repo.owner;
		this.name = repo.name;
		this.url = repo.url ?? `https://github.com/${repo.owner}/${repo.name}`;
	}
}

export const gitHubRepo_MenuBar_Item = ({
	label,
	repo,
}: {
	label: string;
	repo: GitHubRepo;
}) => {
	const { owner, name, url } = repo;

	return openUrlMenuItem({
		label,
		url: url ?? `https://github.com/${owner}/${name}`,
	});
};

export class GitHubIssue {
	assignees?: string = '';
	labels?: string = '';
	template?: string = '';
	title?: string = '';

	constructor(issue: GitHubIssue) {
		this.assignees = issue.assignees;
		this.labels = issue.labels;
		this.template = issue.template;
		this.title = issue.title;
	}
}

export const get_issue_url = (repo: GitHubRepo, issue: GitHubIssue) => {
	const issue_properties = new Map(Object.entries(issue));
	const query = form_query(issue_properties);
	const issue_url = `https://github.com/${repo.owner}/${repo.name}/issues/new?${query}`;
	return issue_url;
};

interface IssueTemplate_MenuBar {
	label: string;

	repo: GitHubRepo;
	issue: GitHubIssue;
}

export const gitHubIssueFromTemplate = (template: IssueTemplate_MenuBar) => {
	const { label, repo, issue } = template;
	return openUrlMenuItem({
		label,
		url: get_issue_url(repo, issue),
	});
};
