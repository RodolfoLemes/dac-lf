import json
from domain.response import Response
from service import draw_card

def lambda_handler(event, context):
    response: Response = None
    try:
        print(event)
        body = json.loads(event['body'])

        level = body.get('level', 1)
        method = body.get('method', 'sigmoid')

        print(f"level: {level}, method: {method}")

        card = draw_card.draw_door(level, method)
        response = Response(200, data=card)
    except ValueError as e:
        response = Response(400, err_message=str(e))
    except Exception as e:
        response = Response(500, err_message=str(e))

    print(response.to_json())
    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.to_json())
    }

## tests
## resp = lambda_handler({'body': '{"level": 1, "method": "sigmoid"}'}, None)
## print(resp)