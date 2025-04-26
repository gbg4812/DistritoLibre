# Wiki

<!--toc:start-->

- [Wiki](#wiki)
  - [API](#api)
    - [Urls Overview](#urls-overview)
    - [Posts](#posts)
      - [Get list of posts (title, author, icon, firstlines) containing tag _tag name_, section tag _stag name_ and building tag _btag name_](#get-list-of-posts-title-author-icon-firstlines-containing-tag-tag-name-section-tag-stag-name-and-building-tag-btag-name)
      - [Get a particular post (title, author, icon, content, stags, btags, tags)](#get-a-particular-post-title-author-icon-content-stags-btags-tags)
      - [Get a list of btags for the stag](#get-a-list-of-btags-for-the-stag)
      - [Post new post (title, author, icon, content (file), tags)](#post-new-post-title-author-icon-content-file-tags)
      - [Delete post (title)](#delete-post-title)
    - [Auth](#auth)
  - [Usage Stories](#usage-stories) - [Playful exploration of posts](#playful-exploration-of-posts) - [Search of post](#search-of-post) - [Login](#login) - [Logout](#logout) - [New Post](#new-post)
  <!--toc:end-->

## API

### Urls Overview

- /posts/\* # urls realted to posts
- /auth/\* # urls realted to auth

### Posts

#### Get list of posts (title, author, icon, firstlines) containing tag _tag name_, section tag _stag name_ and building tag _btag name_

| Url      | /posts/?tag=_tag name_?stag=_stag name_?btag=_btag name_ |
| -------- | -------------------------------------------------------- |
| response | PostOverviewList                                         |

```ts
interface PostOverview = {
    title: string;
    author: {
        username: string;
    };
    icon: URL;
    description: string;
    tags : [index : number] : string;
};

interface PostOverviewList = {
    [index: number]: PostOverview;
};
```

#### Get a particular post (title, author, icon, content, stags, btags, tags)

| Url      | /posts/\<str : title\>/ - /posts/ |
| -------- | --------------------------------- |
| response | Post                              |

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

#### Get a list of btags for the stag

Gets the list of btags that apear in at least one post with the stag

| Url      | /posts/btags/\<str : stag\>/ |
| -------- | ---------------------------- |
| response | BTagList                     |

```ts
interface Tag {
  name: string;
}

interface BTag extends Tag {
  icon: URL;
}

interface BTagList {
  [index: number]: BTag;
}
```

#### Post new post (title, author, icon, content (file), tags)

| Url      | /posts/new/   |
| -------- | ------------- |
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

#### Delete post (title)

| Url      | /posts/delete/\<str : title\>/ |
| -------- | ------------------------------ |
| response | StateResponse                  |
| auth     | required                       |

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
