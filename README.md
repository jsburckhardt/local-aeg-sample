# local-aeg-sample
az login



create eventgrid topic 
az group create --name laeg-rg0001 --location eastus
az eventgrid topic create --resource-group laeg-rg0001 --name laegt0001 -l eastus

create function local
func init LocalEventGridFunctionProj --python
func new --name EventGridTriggered --template "Azure Event Grid trigger"

create az function and deploy it
az storage account create --name laegfasa0001 --resource-group laeg-rg0001
az functionapp create --resource-group laeg-rg0001 --consumption-plan-location eastus --runtime python --runtime-version 3.8 --functions-version 3 --name laegfa0001 --os-type linux --storage-account laegfasa0001
func azure functionapp publish laegfa0001



ngrok
ngrok authtoken <key from your account>
ngrok http -host-header=localhost 7071



create eventgrid subscriptions
topic_id=$(az eventgrid topic show --resource-group laeg-rg0001 --name laegt0001 --query id -o tsv)
function_endpoint=$(az functionapp function show --resource-group laeg-rg0001 --name laegfa0001 --function-name EventGridTriggered --query id -o tsv)
az eventgrid event-subscription create --name laegtsubs0001 \
    --source-resource-id $topic_id \
    --endpoint $function_endpoint \
    --endpoint-type azurefunction


az storage account create --name laegsa0001 --resource-group laeg-rg0001
export EVENT_GRID_STORAGE_CONNECTION=$(az storage account show-connection-string --name laegsa0001 --resource-group laeg-rg0001 -o tsv)
event-grid-local subscribe
event-grid-local start