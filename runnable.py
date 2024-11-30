from main import CanvasAPI
import sys

if __name__ == '__main__':
    user_id = int(sys.argv[1])
    api = CanvasAPI(user_id=user_id)
    api.UserAssignmentView()
    sys.stdout.flush()