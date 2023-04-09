from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class login(viewsets.ViewSet):
    



    # getAll
    # GET /api/v1/login/
    def list(self, request, format=None):
        return Response('getAll NOT IMPLEMENTED',status=status.HTTP_200_OK)
    
    # getOneById
    # GET /api/v1/login/{pk}/
    def retrieve(self, request, pk=id):
        return Response('getOneById NOT IMPLEMENTED',status=status.HTTP_200_OK)

    # # saveOne
    # # POST /api/v1/login/
    # # def create(self, request):
    # #     return Response('saveOne NOT IMPLEMENTED',status=status.HTTP_200_OK)
    
    # # updateOneById
    # # PUT /api/v1/login/{pk}/
    # def update(self, request, pk=None):
    #     return Response('updateOneById NOT IMPLEMENTED',status=status.HTTP_200_OK)

    # # deleteOneById
    # # DELETE /api/v1/login/{pk}/
    # def destroy(self, request, pk=None):
    #     return Response('deleteOneById NOT IMPLEMENTED',status=status.HTTP_200_OK)
    
    # ## ADITIONAL ENDPOINTS

    
    # # getOneById
    # # get /api/v1/login/getOneById/{pk}
    # @action(methods=["get"], detail=True)
    # def get(self, request, pk=None):
    #     return Response('NOT IMPLEMENTED geet',status=status.HTTP_200_OK)

    # # saveOne
    # # post /api/v1/login/saveOne/
    # @action(methods=['post'], detail=False)
    # def post(self, request, pk=None):
    #     return Response('NOT IMPLEMENTED ppppost',status=status.HTTP_200_OK)
    
    # # updateOneById
    # # put /api/v1/login/put
    # @action(methods=['put'], detail=False)
    # def put(self, request, pk=None):
    #     return Response('NOT IMPLEMENTED PPPPPPPPPPPUT',status=status.HTTP_200_OK)

    # # post /api/v1/login/1/example/
    # @action(methods=['post'], detail=True, )
    # def example(self, request, pk=None):
    #     return Response('NOT IMPLEMENTED',status=status.HTTP_200_OK)

    # ## TEST GENERACION	
    # # GET /api/v1/login/create/
    # @action(methods=["get","post","delete"], detail=False,url_path="create")
    # def route(self, request):
    #     return Response('NOT IMPLEMENTED CREATE',status=status.HTTP_200_OK)
    
    # GET /api/v1/login/test/
    @action(methods=["get"], detail=False, url_path="test")  
    def route(self, request): 
	    return Response('NOT IMPLEMENTED get test ROUTE',status=status.HTTP_200_OK)
    
    # # POST /api/v1/login/test/
    # @action(methods=["post"], detail=False, url_path="test")  
    # def route1(self, request):
	#     return Response('NOT IMPLEMENTED post test ROUTE',status=status.HTTP_200_OK)

