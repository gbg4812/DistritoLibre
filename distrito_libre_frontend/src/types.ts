export interface TagList {
    [index: number]: string;
}

export interface PostOverview {
    title: string;
    author: {
        username: string;
    };
    icon: string;
    description: string;
    tags: TagList;
}

export interface PostOverviewList {
    [index: number]: PostOverview;
}

export interface Post {
    title: string;
    author: {
        username: string;
    };
    icon: string;
    description: string;
    content: string;
    tags: TagList;
}

export interface Tag {
    name: string;
}

export interface BTag extends Tag {
    icon: URL;
}

export interface BTagList {
    [index: number]: BTag;
}

export interface StateResponse {
    state: number;
    message?: string;
}

export interface UserCredentials {
    username: string;
    password: string;
}

export interface UserInfo {
    username: string;
    password: string;
    email: string;
}
