# Start Minikube (if using local Kubernetes)
minikube start

# Deploy the website
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Check the status
kubectl get pods
kubectl get services
