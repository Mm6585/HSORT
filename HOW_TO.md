### Installation
```
$ git clone 
$ cd HSORT
$ pip install -r requirements.txt
```
### Get Firebase Realtime DB key
1. https://console.firebase.google.com/
2. create your project
3. create your realtime DB (test mode)
4. open project setting -> service account -> generate private key
5. save your key.json file "HSORT/key/key.json"

### Test
```
$ python track.py --source test.mp4 --room-no [anything] --max-id [int>=17] --strong-sort-weights resnet50_fc512_msmt17.pt
```

*****

