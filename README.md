# clickup-python
ClickUp API wrapper written in python

## Installing
```
pip install clickup-python
```
## Before start
To use ClickUp Python, go to settings, integration and create a 'New App', copy the CLIENT_ID and CLIENT_SECRET, finally setup the Redirect URL
https://app.clickup.com/{team_id}/settings/team/{team_id}/integrations?integration=api

## Usage
### Client instantiation
```
from clickuppython.client import Client
client = Client(CLICKUP_CLIENT_ID, CLICKUP_CLIENT_SECRET)
```

### OAuth 2.0
#### Get authorization url
```
authorization_url = client.authorization_url(redirect_uri)
```

#### Exchange the code for an access token
```
response = client.exchange_code(code)
```

#### Set token
```
client.set_token(token)
```

### ClickUp Workflow
#### Get Workspace
```
response = client.get_workspace()
#Returns
{
    "teams": [
        {
            "id": "team_id",
            "name": "Gearplug Test",
            "color": "#ff4081",
            "avatar": "None",
            "members": [
                {
                    "user": {
                        "id":user_id,
                        "username": "gearplug",
                        "email": "example@gearplug.io",
                        "color": "#81b1ff",
                        "profilePicture": "None",
                        "initials": "JS",
                        "role": 1,
                        "custom_role": "None",
                        "last_active": "1646340664585",
                        "date_joined": "1646059972931",
                        "date_invited": "1646059972931"
                    }
                }
            ]
        }
    ]
}
```

#### Get Spaces
```
#Use the Id from previous response to get the available Spaces list
response = client.get_spaces(team_id)

#Returns
{
    "spaces": [
        {
            "id": "space_id",
            "name": "Gearplug Test Space 2",
            "private": false,
            "statuses": [
                {
                    "id": "status_id",
                    "status": "to do",
                    "type": "open",
                    "orderindex": 0,
                    "color": "#d3d3d3"
                },
                {
                    "id": "id",
                    "status": "progress",
                    "type": "custom",
                    "orderindex": 1,
                    "color": "#3397dd"
                },
                {
                    "id": "id",
                    "status": "complete",
                    "type": "closed",
                    "orderindex": 2,
                    "color": "#6bc950"
                }
            ],
            "multiple_assignees": true,
            "features": {
                "due_dates": {
                    "enabled": true,
                    "start_date": true,
                    "remap_due_dates": false,
                    "remap_closed_due_date": false
                },
                "sprints": {
                    "enabled": false
                },
                "time_tracking": {
                    "enabled": true,
                    "harvest": false,
                    "rollup": false
                },
                "points": {
                    "enabled": false
                },
                "custom_items": {
                    "enabled": false
                },
                "priorities": {
                    "enabled": true,
                    "priorities": [
                        {
                            "id": "1",
                            "priority": "urgent",
                            "color": "#f50000",
                            "orderindex": "1"
                        },
                        {
                            "id": "2",
                            "priority": "high",
                            "color": "#ffcc00",
                            "orderindex": "2"
                        },
                        {
                            "id": "3",
                            "priority": "normal",
                            "color": "#6fddff",
                            "orderindex": "3"
                        },
                        {
                            "id": "4",
                            "priority": "low",
                            "color": "#d8d8d8",
                            "orderindex": "4"
                        }
                    ]
                },
                "tags": {
                    "enabled": true
                },
                "check_unresolved": {
                    "enabled": true,
                    "subtasks": "None",
                    "checklists": "None",
                    "comments": "None"
                },
                "zoom": {
                    "enabled": false
                },
                "milestones": {
                    "enabled": false
                },
                "custom_fields": {
                    "enabled": true
                },
                "dependency_warning": {
                    "enabled": true
                },
                "multiple_assignees": {
                    "enabled": true
                }
            },
            "archived": false
        }
    ]
}


```

#### Get Folders
```
#Use the Id from previous response to get the available Folder list
response = client.get_folder(space_id)
#Returns
{
    "folders": [
        {
            "id": "id",
            "name": "folder 1",
            "orderindex": 1,
            "override_statuses": false,
            "hidden": false,
            "space": {
                "id": "id",
                "name": "Gearplug Test Space 2"
            },
            "task_count": "1",
            "archived": false,
            "statuses": [],
            "lists": [
                {
                    "id": "id",
                    "name": "List",
                    "orderindex": 0,
                    "status": "None",
                    "priority": "None",
                    "assignee": "None",
                    "task_count": 1,
                    "due_date": "None",
                    "start_date": "None",
                    "space": {
                        "id": "id",
                        "name": "Gearplug Test Space 2",
                        "access": true
                    },
                    "archived": false,
                    "override_statuses": "None",
                    "statuses": [
                        {
                            "id": "id",
                            "status": "to do",
                            "orderindex": 0,
                            "color": "#d3d3d3",
                            "type": "open"
                        },
                        {
                            "id": "id",
                            "status": "progress",
                            "orderindex": 1,
                            "color": "#3397dd",
                            "type": "custom"
                        },
                        {
                            "id": "id",
                            "status": "complete",
                            "orderindex": 2,
                            "color": "#6bc950",
                            "type": "closed"
                        }
                    ],
                    "permission_level": "create"
                }
            ],
            "permission_level": "create"
        }
    ]
}
```

#### Get Lists
```
#Use the Id from previous response to get the available Lists
response = client.get_list(space_id)

#Returns
{
    "lists": [
        {
            "id": "id",
            "name": "List",
            "orderindex": 0,
            "status": "None",
            "priority": "None",
            "assignee": "None",
            "task_count": 1,
            "due_date": "None",
            "start_date": "None",
            "folder": {
                "id": "id",
                "name": "folder 1",
                "hidden": false,
                "access": true
            },
            "space": {
                "id": "id",
                "name": "Gearplug Test Space 2",
                "access": true
            },
            "archived": false,
            "override_statuses": "None",
            "permission_level": "create"
        }
    ]
}
```

#### Get Tasks
```
#Use the Id from previous response to get the available Task list
response = client.get_tasks(space_id)

#Response
{
    "tasks": [
        {
            "id": "id";
                "custom_id": "None",
            "name": "task 1",
            "text_content": "None",
            "description": "None",
            "status": {
                "status": "to do",
                "color": "#d3d3d3",
                "type": "open",
                "orderindex": 0
            },
            "orderindex": "7221303.00017640000000000000000000000000",
            "date_created": "1646261029519",
            "date_updated": "1646261044142",
            "date_closed": "None",
            "archived": false,
            "creator": {
                "id": "id";
                    "username": "Johann Sebastián",
                "color": "#81b1ff",
                "email": "mail",
                "profilePicture": "None"
            },
            "assignees": [
                {
                    "id": "id";
                    "username": "Johann Sebastián",
                    "color": "#81b1ff",
                    "initials": "JS",
                    "email": "mail",
                    "profilePicture": "None"
                }
            ],
            "watchers": [],
            "checklists": [],
            "tags": [],
            "parent": "None",
            "priority": "None",
            "due_date": "None",
            "start_date": "None",
            "points": "None",
            "time_estimate": "None",
            "custom_fields": [],
            "dependencies": [],
            "linked_tasks": [],
            "team_id": "id",
            "url": "https://app.clickup.com/t/task_id",
            "permission_level": "create",
            "list": {
                "id": "id";
                    "name": "List",
                "access": true
            },
            "project": {
                "id": "id";
                    "name": "folder 1",
                "hidden": false,
                "access": true
            },
            "folder": {
                "id": "id";
                    "name": "folder 1",
                "hidden": false,
                "access": true
            },
            "space": {
                "id": "id";
            }
        }
    ]
}
```

#### Create Task
```
#Use the Id from list_id response to get the available Task list
response = client.create_task(list_id)
#Return
{
    "name":"New Task Name",
    "description":"New Task Description",
    "assignees":[
        183
    ],
    "tags":[
        "tag name 1"
    ],
    "status":"Open",
    "priority":3,
    "due_date":1508369194377,
    "due_date_time":false,
    "time_estimate":8640000,
    "start_date":1567780450202,
    "start_date_time":false,
    "notify_all":true,
    "parent":null,
    "links_to":null,
    "check_required_custom_fields":true,
    "custom_fields":[
        {
            "id":"id",
            "value":23
        },
        {
            "id":"id",
            "value":"Text field input"
        }
    ]
}

```
#### Update Task
```
#Use the Id from task_id response to get the available Task list
response = client.update_task(task_id)
#Return
{
    "id": "9hx",
    "custom_id": null,
    "name": "Updated Task Name",
    "text_content": "Updated Task Content",
    "description": "Updated Task Content",
    "status": {
        "status": "in progress",
        "color": "#d3d3d3",
        "orderindex": 1,
        "type": "custom"
    },
    "archived": false,
    "orderindex": "1.00000000000000000000000000000000",
    "date_created": "1567780450202",
    "date_updated": "1567780450202",
    "date_closed": null,
    "creator": {
        "id": 183,
        "username": "John Doe",
        "color": "#827718",
        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
    },
    "assignees": [],
    "checklists": [],
    "tags": [],
    "parent": "abc1234",
    "priority": null,
    "due_date": null,
    "start_date": null,
    "time_estimate": null,
    "time_spent": null,
    "list": {
        "id": "123"
    },
    "folder": {
        "id": "456"
    },
    "space": {
        "id": "789"
    },
    "url": "https://app.clickup.com/t/9hx"
}
```

#### Create Webhook
```
#Use the Id from task_id response to get the available Task list
response = client.create_webhook(task_id, team_id, endpoint, event)
#Return
{
    {
        "event": "taskStatusUpdated",
        "history_items": [
            {
                "id": id,
                "type": 1,
                "date": "1646350890907",
                "field": "status",
                "parent_id": id,
                "data": {
                    "status_type": "custom"
                },
                "source": null,
                "user": {
                    "id": id,
                    "username": "Johann Sebastián",
                    "email": "mail",
                    "color": "#81b1ff",
                    "initials": "JS",
                    "profilePicture": null
                },
                "before": {
                    "status": "complete",
                    "color": "#6bc950",
                    "orderindex": 2,
                    "type": "closed"
                },
                "after": {
                    "status": "progress",
                    "color": "#3397dd",
                    "orderindex": 1,
                    "type": "custom"
                }
            }
        ],
        "task_id": id,
        "webhook_id": id
    }
```
#### Delete Webhook
```
#Use the Id from task_id response to get the available Task list
response = client.delete_webhook(webhook_id)
```

## Requirements
- requests

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.

#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/clickup-python/issues).

#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/clickup-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')   
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
