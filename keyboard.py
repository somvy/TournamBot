#reg_st=1
keyboard_dict_first_dialog_1 = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Да!"
        },
        "color": "positive"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "Нет("
        },
        "color": "negative"
      }]
    ]
  }
#reg_st=2
keyboard_dict_first_dialog_not = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Ладно, уговорили!"
        },
        "color": "positive"
      }],[
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "\"Ладно,уговорили\" только другого цвета"
        },
        "color": "negative"
      }]
    ]
  }
#reg_st=3
keyboard_dict_first_dialog_ok = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "1"
        },
        "color": "primary"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "2"
        },
        "color": "primary"
      }]
    ]
  }

keyboard_dict_thanks = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Спасибо!"
        },
        "color": "positive"
      }]
    ]
  }

keyboard_dict_last_solo = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Изменить статус участника"
        },
        "color": "primary"
      }],
      [
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "Отменить регистрацию в турнире"
        },
        "color": "negative"
      }],
      [
      {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"3\"}",
            "label": "Беседа для solo игроков"
                  },
        "color": "positive"

      }
      ]
    ]
  }
  
keyboard_dict_noth = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "😉"
        },
        "color": "positive"
      }]
    ]
  }

keyboard_dict_first_dialog_ok = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "1"
        },
        "color": "primary"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "2"
        },
        "color": "primary"
      }]
    ]
  }

keyboard_dict_last_team = {
    "one_time": None,
    "buttons": [
      [
      {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Изменить статус участника"
        },
        "color": "primary"
       }
      ],
      [
       {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "Отменить регистрацию в турнире"
        },
        "color": "negative"
       }
      ]
    ]
  }
  
keyboard_dict_ausure = {
    "one_time": None,
    "buttons": [
      [
      {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Нет"
        },
        "color": "positive"
       }
      ],
      [
       {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "Да"
        },
        "color": "negative"
       }
      ]
    ]
  }
keyboard_dict_ok = {
    "one_time": None,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": "Хорошо"
        },
        "color": "positive"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": "Ладно"
        },
        "color": "negative"
      }]
    ]
  }