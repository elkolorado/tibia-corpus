# json schema
conversations_schema =  {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Conversations",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "file": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "conversation": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string"
            },
            "answer": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "prompt",
            "answer"
          ]
        }
      }
    },
    "required": [
      "file",
      "name",
      "conversation"
    ]
  }
}
npc_dialogues_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "job": {
        "type": "string"
      },
      "race": {
        "type": "string"
      },
      "gender": {
        "type": "string"
      },
      "location": {
        "type": "string"
      },
      "subarea": {
        "type": "string"
      },
      "map": {
        "type": "string"
      },
      "version": {
        "type": "string"
      },
      "quests": {
        "type": "array",
        "items": {}
      },
      "dialogues": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "coordinates": {
        "type": "array",
        "items": {
          "type": "number"
        }
      }
    },
    "required": [
      "name",
      "job",
      "race",
      "gender",
      "location",
      "subarea",
      "map",
      "version",
      "quests",
      "dialogues",
      "coordinates"
    ]
  }
}
books_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "author": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "locations": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "libraries": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "version": {
        "type": "string"
      },
      "related-articles": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "next-book": {
        "type": "string"
      },
      "previous-book": {
        "type": "string"
      },
      "img": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "text": {
        "type": "string"
      },
      "map": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "type": {
        "type": "string"
      },
      "locations-wip": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "mainarea": {
              "type": "string"
            },
            "area": {
              "type": "string"
            },
            "subarea": {
              "type": "string"
            }
          },
          "required": [
            "mainarea",
            "area",
            "subarea"
          ]
        }
      }
    },
    "required": [
      "name",
      "author",
      "description",
      "locations",
      "libraries",
      "version",
      "related-articles",
      "next-book",
      "previous-book",
      "img",
      "text",
      "map",
      "type",
      "locations-wip"
    ]
  }
}
