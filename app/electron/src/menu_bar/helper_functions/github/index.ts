import { openUrlMenuItem } from 'electron-util';

import { formQuery } from './urls';

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

export const githubRepoMenuBarItem = ({
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

export const urlQuote = (url: string) => {
	const words = url.split(' ');
	return words.join('+');
};

export class GitHubIssue {
	assignees?: string = '';
	labels?: string = '';
	template?: string = '';
	title?: string = '';

	constructor(issue: GitHubIssue) {
		this.assignees = urlQuote(issue.assignees ?? '');
		this.labels = urlQuote(issue.labels ?? '');
		this.template = urlQuote(issue.template ?? '');
		this.title = urlQuote(issue.title ?? '');
	}
}

export const getIssueUrl = (repo: GitHubRepo, issue: GitHubIssue) => {
	const issueProperties = new Map(Object.entries(issue));
	const query = formQuery(issueProperties);
	const issueUrl = `https://github.com/${repo.owner}/${repo.name}/issues/new?${query}`;
	return issueUrl;
};

interface IssueTemplateMenuBar {
	label: string;

	repo: GitHubRepo;
	issue: GitHubIssue;
}

export const gitHubIssueFromTemplate = (template: IssueTemplateMenuBar) => {
	const { label, repo, issue } = template;
	return openUrlMenuItem({
		label,
		url: getIssueUrl(repo, issue),
	});
};
