class ReturnDTO:
    def __init__(self, has_success=False, result_msg=None, obj=None):
        self.result_msg = result_msg
        self.has_success = has_success
        self.object = obj
