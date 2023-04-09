from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..middlewares.validateAuth import validateAuth
from django.utils.decorators import method_decorator


class login(viewsets.ViewSet):

    @method_decorator(validateAuth)
    def list(self, request, format=None, detail=False):
        print('get list')
        print(request.query_params)
        return Response('NOT IMPLEMENTED getAll',status=status.HTTP_200_OK)
        
    @method_decorator(validateAuth)
    def retrieve(self, request, pk=None, detail=False):
        # print(request.headers)
        # print(request.body)
        # pk=parameter
        print('get retrieve')
        return Response('NOT IMPLEMENTED getOneById aaaa',status=status.HTTP_200_OK)

    # GET /api/v1/login/casa/
    @method_decorator(validateAuth)
    @action(methods=["get"], detail=False, url_path="casa")  
    def route2(self, request): 
	    return Response('NOT IMPLEMENTED get test ROUTE',status=status.HTTP_200_OK)

    # get /api/v1/login/createExample/
    
    # @action(methods=['get'], detail=False)
    # # @permission_classes([IsAuthenticated, ])
    # def createExample(self, request):
    #     return Response('createExample',status=status.HTTP_200_OK)

    # # post /api/v1/login/post
    # @action(methods=['get'], detail=False)
    # def post(self, request, pk=None):
    #     return Response('example post',status=status.HTTP_200_OK)
        

    # # post /api/v1/login/1/example/
    # @action(methods=['get'], detail=True)
    # def example(self, request, pk=id):
    #     return Response('example detailed post',status=status.HTTP_200_OK)
    
    # # GET /api/v1/login/auto/
    # @action(methods=["get"], url_path="auto", detail=True)  
    # def route1(self, request, canal=None, pk=None, format=None): 
    #     return Response('NOT IMPLEMENTED auto getOneById',status=status.HTTP_200_OK)

    # # GET /api/v1/login/casa/
    # @action(methods=["get"], detail=False, url_path="casa")  
    # def route2(self, request): 
	#     return Response('NOT IMPLEMENTED get test ROUTE',status=status.HTTP_200_OK)


    