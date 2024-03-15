from flask import Flask,  redirect, url_for,render_template,request
from fuzzywuzzy import fuzz, process

app=Flask(__name__)

defined_responses=[
    'hi',
    'hello',
    'what are the courses offered ?',
    'where can I find the curricullum?',
    'what is the syllabus for btech diploma',
    'what is the procedure to apply for admissions?',
    'what are the scholarship provisions?',
    'what about the research opportunities being provided?',
    'what are the different events I can take part in?',
    'What facilities are provided in hostels?',
    'Are hostel facilities being provided?',
    'What is the condition of labs?',
    'Is library sufficient to handle all these students?',
    'Okay thanks for the help goodbye'
]
def process_manager(user_message):
    match,score=process.extractOne(user_message.lower(),defined_responses,scorer=fuzz.token_set_ratio)
    return [match,score]
@app.route('/',methods=['GET','POST'])
def main():
    user_messages=[]
    bot_messages=[]
    dataset={ #greeting messages: 
             'hi':'Hello how may i help you',
             'hello':'Glad you reached out! feel free to ask your queries',
             
             #course information related queries:
             'what are the courses offered ?':'Currently, the courses offered in the department of CSE are BTech in CSE(core as well as specialised domains) and diploma in cse. However the courses offered by the university are in vast domains and you may have a look on the university website for better understanding',
             'where can I find the curricullum?':'The curricullum can be found on the department website :)',
             'what is the syllabus for btech diploma':'The curricullum can be found on the department website :)',

             #admission related queries:
             'what is the procedure to apply for admissions?':'The process is quite simple. You may register through the university website and after registration is completed, you may proceed with the admission process itself. For more details, check the university website or contact us in person',
             'what are the scholarship provisions?':'Scholarships are offered based on your previous academic performances. For more information check the university website.',
             
             #research related queries:
             'what about the research opportunities being provided?':'You will get ample opportunities for research in any domains. We have a dedicated research cell which handles all the research related things.',
             
             #queries regarding events being conducted:
             'what are the different events I can take part in?':'Various extracurricular activities are organised by the university. Talking of the opportunities you will get from the department side, we have various hackathons, seminars, workshops etc. which will help you enhance your skills and knowledge',
             
             #infrastructure regarding libraries, labs, hostels etc.
             'Are hostel facilities being provided?':'Our hostels are one of the best hostels you can find yourself in. We provide all the facilities in the hostels ranging from proper water and electricity supply, air condotioned rooms, fast wifi etc.',
             'What facilities are provided in hostels?':'We provide all the facilities in the hostels ranging from proper water and electricity supply, air condotioned rooms, fast wifi etc.',
             'What is the condition of labs?':'We have fantastic labs to assist students with their practical knowledge. Fast internet connections and up to date systems working on linux based os will help you a lot',
             'Is library sufficient to handle all these students?':'Our library has adequate books to suffice the number of students present in the campus. Moreover, we also provide facility of digital library in case you want to explore something beyond',

             #concluding regards:
             'Okay thanks for the help goodbye':'No issues!! Feel free to connect the next time you have any confusions, Have a great day! :)'
            }
    if request.method=='POST':
        user_message=request.form["message"]
        processed_items=process_manager(user_message)
        if processed_items[1]>60:
          bot_message=dataset[processed_items[0]]
        else:
            bot_message="Sorry I cannot find anything relevant to this"
        user_messages.append(user_message)
        bot_messages.append(bot_message)
        
    return render_template('index.html',user_messages=user_messages, bot_messages=bot_messages)
if __name__=="__main__":
    app.run(debug=True)