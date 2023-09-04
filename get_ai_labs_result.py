import sys
import ai21

ai21.api_key = <API_KEY_FIND_IT_https://studio.ai21.com/account/api-key>
prompt = ' '.join(sys.argv[1:])

# J2 Ultra
response_ultra = ai21.Completion.execute(
    model="j2-ultra",
    prompt=prompt,
    numResults=1,
    maxTokens=500,
    temperature=0.7,
    topKReturn=0,
    topP=1,
    stopSequences=["##"]
)

print(response_ultra['completions'][0]['data']['text'])
