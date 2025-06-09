export interface PostOverview {
    id: number;
    title: string;
    author: {
        username: string;
    };
    icon: string;
    description: string;
    tags: Tag[];
}

export interface Post {
    id: number;
    title: string;
    author?: {
        username: string;
    };
    icon: string;
    description: string;
    content: string;
    tags: Tag[];
}

export interface Tag {
    name: string;
}

export interface BTag extends Tag {
    icon: string;
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
    password?: string;
    email: string;
}
