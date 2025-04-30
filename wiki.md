# Wiki

<!--toc:start-->

- [Wiki](#wiki)
  - [API](#api)
    - [Urls Overview](#urls-overview)
    - [Posts](#posts)
      - [Get list of posts (title, author, icon, firstlines) containing tags _tag name_](#get-list-of-posts-title-author-icon-firstlines-containing-tags-tag-name)
      - [Get a particular post (title, author, icon, content, tags)](#get-a-particular-post-title-author-icon-content-tags)
      - [Delete post (title)](#delete-post-title)
      - [Post new post (title, author, icon, content (file), tags)](#post-new-post-title-author-icon-content-file-tags)
      - [Get a list of btags for the stag](#get-a-list-of-btags-for-the-stag)
    - [Auth](#auth)
      - [Initiate login session](#initiate-login-session)
      - [Logout User](#logout-user)
      - [Set and get user info](#set-and-get-user-info)
  - [Usage Stories](#usage-stories) - [Playful exploration of posts](#playful-exploration-of-posts) - [Search of post](#search-of-post) - [Login](#login) - [Logout](#logout) - [New Post](#new-post)
  <!--toc:end-->

## API

### Urls Overview

- /posts/\* # urls realted to posts
- /auth/\* # urls realted to auth

### Posts

#### Get list of posts (title, author, icon, firstlines) containing tags _tag name_

| Url      | /posts/?tag=_tag name_?tag=_tag name_?tag=_tag name_ |
| -------- | ---------------------------------------------------- |
| HTTP     | GET                                                  |
| response | PostOverviewList                                     |

```ts
interface PostOverview = {
    title: string;
    author: {
        username: string;
        email: string;
    };
    icon: URL;
    content: string;
    tags : [index : number] : string;
};

interface PostOverviewList = {
    [index: number]: PostOverview;
};
```

#### Get a particular post (title, author, icon, content, tags)

| Url      | /posts/detail/\<str : title\>/ |
| -------- | ------------------------------ |
| HTTP     | GET                            |
| response | Post                           |

```ts
interface Post {
    title: string;
    author: {
        username: string;
    };
    icon: URL;
    content: string;
    tags : [index : number] : string;
};
```

#### Delete post (title)

| Url      | /posts/detail/\<str : title\>/ |
| -------- | ------------------------------ |
| HTTP     | DELETE                         |
| response | StateResponse                  |
| auth     | required                       |

#### Post new post (title, author, icon, content (file), tags)

| Url      | /posts/new/   |
| -------- | ------------- |
| HTTP     | POST          |
| request  | Post          |
| response | StateResponse |
| auth     | required      |

[!NOTE] The the authenticated user must be the author

```ts
interface StateResponse {
  state: number;
  message?: string;
}
```

| State Code | Meaning               |
| ---------- | --------------------- |
| 0          | Operation Successful  |
| 1          | Alternative operation |
| 2          | Bad Data              |
| 3          | Operation failure     |

#### Get a list of btags for the stag

Gets the list of btags that apear in at least one post with the stag

| Url      | /posts/btags/?tag=_stag name_ |
| -------- | ----------------------------- |
| response | BTagList                      |

```ts
interface Tag {
  name: string;
}

interface BTag extends Tag {
  icon: URL;
}

interface BTagList {
    btags: [index: number]: BTag;
}
```

### Auth

#### Initiate login session

| Url      | /auth/login/    |
| -------- | --------------- |
| request  | UserCredentials |
| response | StateResponse   |

```ts
interface UserCredentials {
  username: string;
  password: string;
}
```

#### Logout User

| Url      | /auth/logout/ |
| -------- | ------------- |
| response | StateResponse |

#### Set and get user info

| Url              | /auth/userinfo/ |
| ---------------- | --------------- |
| response/request | UserInfo        |

```ts
interface UserInfo {
  username: string;
  password: string;
  email: string;
}
```

## Usage Stories

### Playful exploration of posts

1.
2.

### Search of post

1.
2.

### Login

1.
2.

### Logout

1.
2.

### New Post

1.
2.
