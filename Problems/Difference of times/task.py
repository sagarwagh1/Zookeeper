# put your python code here
event_1_Hr = int(input())
event_1_Min = int(input())
event_1_Sec = int(input())
event_2_Hr = int(input())
event_2_Min = int(input())
event_2_Sec = int(input())
event_1 = (event_1_Hr * 60 * 60) + (event_1_Min * 60) + event_1_Sec
event_2 = (event_2_Hr * 60 * 60) + (event_2_Min * 60) + event_2_Sec
diff = event_2 - event_1
print(diff)
