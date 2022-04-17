# MERUKARI SUMMER INTERNSHIP OCR System

I implemented OCR service API server in Merukari summer internship.

this service support **just English OCR**.

## requirement

I implemented it with below. I don't confirm with other enviromnemet due to short time to implement

python = 3.9
docker = 20.10.12

## quick start

Below explain on the basis that you can use docker and python in your environment.

1. Please install some python modules

```bash

pip install -r requirement.txt

```

2. Please build image and run it 

```bash
# Change to docker directory
cd docker 

# Let's build images
docker compose build

# Try to run container
docker compose up -d
cd  ..
```

3. Try to run some api

I had prepared to run api with python code easily.

But you can also confirm with `http://localhost:5000/<api endpoint>` 



Please confirm you are in `/OCR_service` 

- If you want to run 'POST /image-sync'
  ```bash
  python test/client_test.py image-sync --image-path <image path>
  # e.g
  python test/client_test.py image-sync --image-path test/data/test.png
  
  # It may print like below.
  # <Response [200]>
  # {'task_id': '< any id >'}
  ```

- If you want to run 'POST /image'
  ```bash
  python test/client_test.py post-image --image-path <image path>
  
  # It may print like below.
  # <Response [200]>
  #　{'task_id': '< any id >'}
  
  ```

- If you want to run 'GET /image'    
  ```bash
  python test/client_test.py get-image --id < any id >
  
  # It may print like below.
  #　{'task_id': '= Se a Ba\nunnicr\n\nQ......'}
  # or
  #　{'task_id': None}
  ```

- if you want to run 'POST /image' and 'GET /image' at the same time
  
  ```bash
  python test/client_test.py image --image-path test/data/test.png
  # It may print like below.
  # {'task_id': 'ed68fd36-bee7-4ff7-9bc0-224274514e9f'}
  # {'task_id': None}
  ```
  Please send request 'GET /image'

  ```bash
  python test/client_test.py get-image --id < any id >
  
  # It may print like below.
  #　{'task_id': 'Challenge to make OCR!!!'}
  ```

1. clean up 

```bash
cd docker 
docker compose down -t 0

```

## structure

For future versatility, we have divided the API server and the OCR server into two separate container. By doing this, we expect to be able to adapt autoscaling using kubernetes, etc. and not add to the API server.

I using ubuntu as OCR-server container and API-server container. 

And I using MySQL by mysql server and access by sqlalchemy which is python module. 

### data flow

when you request `POST /image-sync`, data-flow is like below.

![POST_image](./README_image/POST_image_sync.png)

when you request `POST /image` and `GET /image`, data-flow is like below.

when the API-server request Image and id to the OCR-server,  the API-server don't wait to come back and return id for user.

I inplement with `python async` for this logic. 

![image](./README_image/image.png)

### Data base

|  column name  |  type       | overview                       |
| ------------- | ----------- | ------------------------------ |
|  id           |  uuid.UUID  | primary key                    |
|  text         |  LONGTEXT   | OCR result                     |
| Image path    | string      | image apth in OCR server       |
| datetime      | datetime    | insert date time of OCR result |

## test

change to ocr_service root 

```bash

pip install pytest
python -m pytest test

```
