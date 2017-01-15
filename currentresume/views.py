from django.http import JsonResponse
from currentresume.models import Resume
from django.views.generic.edit import View
import json

class CurrResumeView(View):
    def get_error_json_response(self, errMsg):
        '''
        @param errMsg: error message
        @return: JsonResponse 400 BAD REQUEST like {'error': errMsg}
        '''
        json_response = {}
        json_response['error'] = errMsg
        return JsonResponse(json_response, status=400)
    
    def get(self, request):
        '''
        Get the most recent resume or error when none exists
        body with current resume like
            200 OK {'resume_body':'Body of the resume'}
        but when resume not exists
            400 BAD REQUEST like {'error': errMsg}
        @return: JsonResponse 
        '''
        try:
            curr_resume = Resume.objects.latest('date_created')
            json_response = {}
            json_response['resume_body'] = curr_resume.resume_body
            return JsonResponse(json_response, status=200)
        except Resume.DoesNotExist:
            return self.get_error_json_response('No resume uploaded yet.')

    def post(self, request):
        '''
        Add a new resume 
        Simple validation before save for length
        upon success
            201 CREATED {'success':'Resume uploaded.'}
        but when some error
            400 BAD REQUEST like {'error': errMsg}
        @return: JsonResponse 
        '''
        try:
            json_data = json.loads(request.body)
            resume_body_data = json_data['resume_body']
            resume_body_length = len(resume_body_data)
            if resume_body_length == 0:
                return self.get_error_json_response('Resume cannot be empty.')
            elif resume_body_length > 500:
                return self.get_error_json_response('Resume too long.')
            else:
                resume = Resume(resume_body=resume_body_data)
                resume = resume.save()
                json_response = {}
                json_response['success'] = 'Resume uploaded.'
                return JsonResponse(json_response, status=201)
        except ValueError:
            return self.get_error_json_response('Invalid json input.')
        except KeyError as e:
            return self.get_error_json_response('Expecting ' + str(e))
        except Exception as e:
            return self.get_error_json_response('Invalid request: ' + str(e))
