# 教程管理 API 文档

本文档描述了 AGI 平台后台管理系统中教程相关的 API 接口。所有接口都以 `/admin` 作为基础路径，需要管理员权限。

## 认证

所有接口都需要在请求头中携带 Bearer Token：

```http
Authorization: Bearer your-token-here
```

## 教程管理

### 创建教程

```http
POST /admin/tutorials
```

#### 请求参数

| 参数 | 类型 | 必填 | 描述 | 示例 |
|------|------|------|------|------|
| title | string | 是 | 教程标题 | "AGI 入门指南" |
| slug | string | 否 | URL 友好的标识符，不填则自动生成 | "agi" |
| description | string | 是 | 教程描述 | "从零开始学习 AGI 开发" |
| collection_id | integer | 是 | 所属集合ID | 1 |
| is_featured | boolean | 否 | 是否推荐，默认false | true |
| status | string/integer | 否 | 状态：0/draft(草稿)，1/published(发布)，默认draft | "published" |
| cover_url | string | 否 | 封面图片URL | "https://example.com/cover.jpg" |
| meta_title | string | 否 | SEO标题 | "AGI入门指南 - 最全面的AGI学习资料" |
| meta_description | string | 否 | SEO描述 | "这是一个从零开始的AGI学习教程..." |
| meta_keywords | string | 否 | SEO关键词 | "AGI,人工智能,教程" |

#### 响应

```json
{
  "code": 201,
  "message": "教程创建成功",
  "data": {
    "id": 1,
    "title": "AGI 入门指南",
    "slug": "agi",
    "description": "从零开始学习 AGI 开发",
    "collection_id": 1,
    "is_featured": true,
    "status": "published",
    "status_text": "已发布",
    "created_at": "2025-01-16T13:00:00.000000Z",
    "updated_at": "2025-01-16T13:00:00.000000Z",
    "collection": {
      "id": 1,
      "title": "LearnAGI",
      "slug": "learnagi"
    }
  }
}
```

### 更新教程

```http
PUT /admin/tutorials/{id}
```
或
```http
PUT /admin/tutorials/{slug}
```

#### 请求参数

与创建教程相同，所有字段都是可选的。

#### 响应

```json
{
  "code": 200,
  "message": "教程更新成功",
  "data": {
    "id": 1,
    "title": "AGI 入门指南（更新）",
    "slug": "agi",
    "description": "从零开始学习 AGI 开发",
    "collection_id": 1,
    "is_featured": true,
    "status": "published",
    "status_text": "已发布",
    "updated_at": "2025-01-16T13:30:00.000000Z",
    "collection": {
      "id": 1,
      "title": "LearnAGI",
      "slug": "learnagi"
    }
  }
}
```

## 章节管理

### 创建章节

```http
POST /admin/tutorials/{tutorialId}/chapters
```
或
```http
POST /admin/tutorials/{tutorialSlug}/chapters
```

#### 请求参数

| 参数 | 类型 | 必填 | 描述 | 示例 |
|------|------|------|------|------|
| title | string | 是 | 章节标题 | "第一章：什么是AGI" |
| description | string | 否 | 章节描述 | "介绍AGI的基本概念" |
| sequence | integer | 否 | 排序序号，默认为当前最大序号+1 | 1 |
| status | string/integer | 否 | 状态：0/draft(草稿)，1/published(发布)，默认draft | "published" |
| meta_title | string | 否 | SEO标题 | "什么是AGI - AGI入门指南" |
| meta_description | string | 否 | SEO描述 | "本章介绍AGI的基本概念..." |
| meta_keywords | string | 否 | SEO关键词 | "AGI,概念,入门" |

#### 响应

```json
{
  "code": 201,
  "message": "章节创建成功",
  "data": {
    "id": 1,
    "title": "第一章：什么是AGI",
    "slug": "J6dSb7rt",
    "description": "介绍AGI的基本概念",
    "sequence": 1,
    "status": "draft",
    "status_text": "草稿",
    "tutorial_id": 1,
    "created_at": "2025-01-16T13:00:00.000000Z",
    "tutorial": {
      "id": 1,
      "title": "AGI 入门指南",
      "slug": "agi",
      "collection": {
        "id": 1,
        "title": "LearnAGI",
        "slug": "learnagi"
      }
    }
  }
}
```

### 更新章节

```http
PUT /admin/chapters/{id}
```
或
```http
PUT /admin/chapters/{slug}
```

#### 请求参数

与创建章节相同，所有字段都是可选的。

### 章节排序

```http
POST /admin/chapters/reorder
```

#### 请求参数

```json
{
  "chapters": [
    {"id": 1, "sequence": 0},
    {"id": 2, "sequence": 1},
    {"id": 3, "sequence": 2}
  ]
}
```

## 小节管理

### 创建小节

```http
POST /admin/tutorials/{tutorialId}/chapters/{chapterId}/sections
```
或
```http
POST /admin/tutorials/{tutorialSlug}/chapters/{chapterSlug}/sections
```

#### 请求参数

| 参数 | 类型 | 必填 | 描述 | 示例 |
|------|------|------|------|------|
| title | string | 是 | 小节标题 | "人工智能的定义" |
| description | string | 否 | 小节描述 | "什么是人工智能？" |
| content_markdown | string | 是 | 小节内容（Markdown） | "人工智能（AI）是..." |
| sequence | integer | 否 | 排序序号，默认为当前最大序号+1 | 1 |
| status | string/integer | 否 | 状态：0/draft(草稿)，1/published(发布)，默认draft | "published" |
| is_free | boolean | 否 | 是否免费，默认false | true |
| meta_title | string | 否 | SEO标题 | "人工智能定义 - AGI入门指南" |
| meta_description | string | 否 | SEO描述 | "详细解释什么是人工智能..." |
| meta_keywords | string | 否 | SEO关键词 | "人工智能,AI,定义" |

#### 响应

```json
{
  "code": 201,
  "message": "小节创建成功",
  "data": {
    "id": 1,
    "title": "人工智能的定义",
    "full_title": "1.1 人工智能的定义",
    "slug": "g9whowt4",
    "description": "什么是人工智能？",
    "content_markdown": "人工智能（AI）是...",
    "sequence": 1,
    "status": "draft",
    "status_text": "草稿",
    "is_free": true,
    "chapter_id": 1,
    "created_at": "2025-01-16T13:00:00.000000Z",
    "chapter": {
      "id": 1,
      "title": "第一章：什么是AGI",
      "slug": "J6dSb7rt",
      "tutorial": {
        "id": 1,
        "title": "AGI 入门指南",
        "slug": "agi"
      }
    }
  }
}
```

### 更新小节

```http
PUT /admin/sections/{id}
```
或
```http
PUT /admin/sections/{slug}
```

#### 请求参数

与创建小节相同，所有字段都是可选的。

### 小节排序

```http
POST /admin/sections/reorder
```

#### 请求参数

```json
{
  "sections": [
    {"id": 1, "sequence": 0},
    {"id": 2, "sequence": 1},
    {"id": 3, "sequence": 2}
  ]
}
```

## 错误响应

所有接口在发生错误时都会返回统一格式的错误响应：

```json
{
  "code": 400,
  "message": "错误信息",
  "data": null
}
```

常见错误码：

- 201: 创建成功
- 200: 请求成功
- 400: 请求参数错误
- 401: 未授权
- 403: 无权限访问
- 404: 资源未找到
- 422: 参数验证失败
- 500: 服务器内部错误

## 注意事项

1. 所有接口都需要管理员权限
2. 大部分资源支持通过 ID 或 slug 访问
3. 创建和更新操作会自动处理 slug 的唯一性
4. 内容支持 Markdown 格式
5. 排序接口支持批量更新，建议一次性提交所有项的顺序
6. 状态字段支持数字(0,1)或字符串(draft,published)格式
7. SEO 相关字段（meta_title, meta_description, meta_keywords）会在未提供时自动生成
