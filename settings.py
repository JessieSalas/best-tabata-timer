import json

settings_json = json.dumps([
    { 'type': 'title',
        'title': 'Customize Workout'},
    
    { 'type': 'bool',
        'title': 'Sound',
        'desc': 'Enables sound cues in the app',
        'section': 'customize',
        'key': 'sound'},

    { 'type': 'numeric',
        'title': 'Prep Time',
        'desc': 'Amount of preparation time (in seconds) at beginning of workout',
        'section': 'customize',
        'key': 'preptime'},

    { 'type': 'numeric',
        'title': 'Reps per Set',
        'desc': 'Amount of repetitions per set',
        'section': 'customize',
        'key': 'reps'},

    { 'type': 'numeric',
        'title': 'Sets',
        'desc': 'Amount of sets',
        'section': 'customize',
        'key': 'sets'},

    { 'type': 'numeric',
        'title': 'Work Time',
        'desc': 'Duration of work interval',
        'section': 'customize',
        'key': 'worktime'},

    { 'type': 'numeric',
        'title': 'Rest Time',
        'desc': 'Duration of rest interval',
        'section': 'customize',
        'key': 'resttime'}
    ])

