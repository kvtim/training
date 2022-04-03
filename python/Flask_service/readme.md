# Flask service
- [About service](#About)
- [How to run](#How_to_run)
___
## <a name="About"></a> About this service
- #### /index -Start page with links to other endpoint services
    ![index.png](resources/index.png)
    ![img.png](resources/index2.png)
- #### /login - OAuth в Google
    ![img.png](resources/login.png)
- #### /get_weather - city input
    ![img.png](resources/get_weather.png)
- #### /list/city - Weather in city for the next 7 days
    ![img.png](resources/list1.png)
    ![img.png](resources/list2.png)
    ![img.png](resources/list3.png)
- #### /city/date - Weather in city for a specific date
    ![img.png](resources/city.png)
- #### /about - Information about you based on information from login
    ![img.png](resources/about.png)
- #### /useragent - Getting information about what OS you are using and what browser you have
    ![img.png](resources/useragent.png)
- #### /logout
  - logout and redirect to /index
      ![img.png](resources/index2.png)
- ---
## <a name="How_to_run"></a> How to run
- 3 ways:
  - [Create docker image locally](#Create_docker_image_locally)
  - [Download from Docker Hub](#Download_from_Docker_Hub)
  - [Run using k8s](#Run_using_k8s)
___
### <a name="Create_docker_image_locally"></a> Create docker image locally
Clone this project using the command:
```
git clone https://github.com/kvtim/training.git
```
Go to the project directory:
```
cd ./python/Flask_service
```
Build docker image:
```
docker build -t flask_service .
```
![img_9.png](resources/img_9.png)
![img.png](resources/img.png)
Run container based on this image:
```
docker run -it -d -p 5000:5000 --env-file ./config/.env_list --name service --rm flask_service  
```
![img_1.png](resources/img_1.png)

You can find this service on [https://localhost:5000](https://localhost:5000/) or [https://127.0.0.1:5000](https://127.0.0.1:5000/)

![img_2.png](resources/img_2.png)
![img_3.png](resources/img_3.png)
To stop container run this command:
```
docker stop service
```
![img_4.png](resources/img_4.png)

---
### <a name="Download_from_Docker_Hub"></a>  Download from Docker Hub
Run this command in your terminal:
```
docker run -it -d -p 5000:5000 --env-file ./config/.env_list --name service --rm kvtim/flask_service  
```
Docker will download the image and run the container
![img_5.png](resources/img_5.png)

You can find this service on [https://localhost:5000](https://localhost:5000/) or [https://127.0.0.1:5000](https://127.0.0.1:5000/)

![img_7.png](resources/img_7.png)
![img_8.png](resources/img_8.png)
To stop container run this command:
```
docker stop service
```
![img_6.png](resources/img_6.png)

---
### <a name="Run_using_k8s"></a> Run using k8s
Clone this project using the command:
```
git clone https://github.com/kvtim/training.git
```
Go to the k8s directory:
```
cd ./python/Flask_service/k8s
```
Start minikube:
```
minikube start
```
Create secret:
```
kubectl apply -f ./secret.yaml 
```
![img_10.png](resources/img_10.png)
Create deployment:
```
kubectl apply -f deployment.yaml  
```
![img_11.png](resources/img_11.png)
Create service:
```
kubectl apply -f service.yaml
```
![img_12.png](resources/img_12.png)
![img_13.png](resources/img_13.png)
Forward port:
```
kubectl port-forward {pod NAME} 5000:5000
```
![img_14.png](resources/img_14.png)

You can find this service on [https://localhost:5000](https://localhost:5000/) or [https://127.0.0.1:5000](https://127.0.0.1:5000/)

![img_15.png](resources/img_15.png)
![img_16.png](resources/img_16.png)
Press ^C to exit:
![img_17.png](resources/img_17.png)
Stop minikube:
```
minikube stop
```
![img_18.png](resources/img_18.png)
