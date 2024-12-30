curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyBZg_vL6AShfmA8hL7yzw4HdqHPzQDtU5Y" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Which shelter should I go to? Turtleback Island Shelter has 430 occupants and 956 beds and they need	Blankets, PPE, Food	and are currently Over Capacity or Sunset Cove Refuge	which has 870 of 1087 beds and needs Power, PPE, Medical Supplies	and is ccurently Closed or Lagoon Bay Emergency Hub	which has 619 beds filled of	649	and needs Power, Blankets, Medical Supplies and is currently	Closed?"}]
    }]
   }'

