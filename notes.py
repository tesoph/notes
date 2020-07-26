import os
from app import app, db
# models
#import os from pml import app port = int(os.environ.get('PORT', 5000)) app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
