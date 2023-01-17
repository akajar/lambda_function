def lambda_handler(event, context):
    payment_data = json.loads(event["body"])
    
    sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN"))
    
    payment_response = sdk.payment().create(payment_data)['response']
    
    #Para el log de CloudWatch
    payment_log = {
        "id": payment_response.get("id"),
        "status": payment_response.get("status"),
        "status_detail": payment_response.get("status_detail"),
    }
    print(payment_log)
    
    return {
        "statusCode": 200,
        "body": json.dumps(payment_response),
    }
