#### Create an action.
```commandline
ibmcloud fn create currency main.py --web true
```

#### Create api.
```commandline
ibmcloud fn api create /currency_api /currency post currency --response-type json
```

