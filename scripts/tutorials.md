# 教程列表 API 文档

## 获取教程列表

### 接口信息

- 请求路径：`/v1/tutorials`
- 请求方法：`GET`
- 接口描述：获取教程列表，支持分页、筛选和排序

### 请求参数

#### 查询参数

| 参数名 | 类型 | 必填 | 描述 | 示例值 |
|--------|------|------|------|---------|
| collection_id | integer | 否 | 按集合ID筛选 | 1 |
| keyword | string | 否 | 按关键词搜索教程标题或描述 | "AGI" |
| is_featured | boolean | 否 | 是否仅返回推荐教程 | true |
| sort | string | 否 | 排序字段，支持 view_count, chapter_count, created_at | "view_count" |
| order | string | 否 | 排序方向，可选 asc 或 desc | "desc" |
| per_page | integer | 否 | 每页返回的数量，默认15 | 15 |
| page | integer | 否 | 分页页码，默认1 | 1 |

### 响应结果

#### 成功响应
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [
      {
        "id": 1,
        "title": "AGI基础教程",
        "slug": "agi-basic-tutorial",
        "description": "深入学习AGI基础知识",
        "collection_id": 1,
        "is_featured": true,
        "view_count": 1000,
        "chapter_count": 5,
        "cover_url": "https://example.com/cover.jpg",
        "author": {
          "id": 1,
          "name": "John Doe",
          "avatar": "https://example.com/avatar.jpg"
        },
        "collection": {
          "id": 1,
          "title": "AGI基础系列",
          "slug": "agi-basic-series"
        },
        "created_at": "2025-01-10T19:45:53Z",
        "updated_at": "2025-01-10T19:45:53Z"
      }
    ],
    "meta": {
      "total": 100,
      "per_page": 15,
      "current_page": 1,
      "last_page": 7,
      "from": 1,
      "to": 15
    }
  }
}
```

#### 错误响应
```json
{
  "code": 422,
  "message": "参数验证错误",
  "errors": {
    "sort": ["排序字段不支持"],
    "order": ["排序方向只能是asc或desc"]
  }
}
```

### 字段说明

#### 教程对象
| 字段名 | 类型 | 描述 |
|--------|------|------|
| id | integer | 教程ID |
| title | string | 教程标题 |
| slug | string | 教程slug（URL友好的标识符） |
| description | string | 教程描述 |
| collection_id | integer | 所属合集ID |
| is_featured | boolean | 是否推荐 |
| view_count | integer | 浏览次数 |
| chapter_count | integer | 章节数量 |
| cover_url | string | 封面图片URL |
| author | object | 作者信息 |
| collection | object | 所属合集信息 |
| created_at | string | 创建时间 |
| updated_at | string | 更新时间 |

### 示例代码

#### JavaScript (Axios)
```javascript
import axios from 'axios';

// 获取推荐教程列表
const getFeaturedTutorials = async () => {
  try {
    const response = await axios.get('/v1/tutorials', {
      params: {
        is_featured: true,
        sort: 'view_count',
        order: 'desc',
        per_page: 10
      }
    });
    return response.data;
  } catch (error) {
    console.error('获取教程列表失败:', error.response?.data || error.message);
    throw error;
  }
};

// 搜索教程
const searchTutorials = async (keyword) => {
  try {
    const response = await axios.get('/v1/tutorials', {
      params: {
        keyword,
        per_page: 15,
        page: 1
      }
    });
    return response.data;
  } catch (error) {
    console.error('搜索教程失败:', error.response?.data || error.message);
    throw error;
  }
};
```

#### TypeScript
```typescript
interface Author {
  id: number;
  name: string;
  avatar: string;
}

interface Collection {
  id: number;
  title: string;
  slug: string;
}

interface Tutorial {
  id: number;
  title: string;
  slug: string;
  description: string;
  collection_id: number;
  is_featured: boolean;
  view_count: number;
  chapter_count: number;
  cover_url: string;
  author: Author;
  collection: Collection;
  created_at: string;
  updated_at: string;
}

interface PaginationMeta {
  total: number;
  per_page: number;
  current_page: number;
  last_page: number;
  from: number;
  to: number;
}

interface TutorialResponse {
  code: number;
  message: string;
  data: {
    items: Tutorial[];
    meta: PaginationMeta;
  };
}

// API 调用函数
async function fetchTutorials(params: {
  collection_id?: number;
  keyword?: string;
  is_featured?: boolean;
  sort?: string;
  order?: 'asc' | 'desc';
  per_page?: number;
  page?: number;
}): Promise<TutorialResponse> {
  try {
    const response = await axios.get<TutorialResponse>('/v1/tutorials', { params });
    return response.data;
  } catch (error) {
    console.error('获取教程列表失败:', error);
    throw error;
  }
}
```

### 注意事项

1. 所有查询参数都是可选的
2. 排序字段(sort)仅支持：view_count, chapter_count, created_at
3. 排序方向(order)仅支持：asc(升序)、desc(降序)
4. 每页数量(per_page)建议不要超过50，以免影响性能
5. 返回的数据包含分页信息，可用于实现分页控件
6. 如果指定了collection_id，将只返回该合集下的教程
