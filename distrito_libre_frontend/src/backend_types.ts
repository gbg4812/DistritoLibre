export enum StateCodes {
    OPERATION_SUCCESSFUL = 0,
    ALTERNATIVE_OPERATION = 1,
    BAD_DATA = 2,
    OPERATION_FAILURE = 3,
}
export interface PostOverview {
    id: number;
    title: string;
    author: {
        username: string;
    };
    creationd: string;
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
    state: StateCodes;
    message?: string;
}

export interface UserCredentials {
    username: string;
    password: string;
}

export interface UserInfo {
    username: string;
    password?: string;
    email?: string;
}
