from google.cloud import secretmanager

def access_secret()->str:
    '''Access secret from Secret Manager'''
    project_id = "seu-projeto-id"
    secret_id = "spotify_api_key"

    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": secret_name})
    secret_value = response.payload.data.decode("UTF-8")
    return secret_value


