
payload = {
    'action':'login',
    'username': 'utkarshkunwar',
    'password': 'Kunwar@Kaggle'
}

def extract_data(url, file_path):
    '''
    method to extract data
    '''
    with session() as c:
        c.post('https://www.kaggle.com/account/login', data = payload)
        with open(file_path, 'w') as handle:
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                haldle.write(block)
                
def main(project_dir):
    '''
    main method
    '''
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    # urls
    train_url = 'https://www.kaggle.com/c/3136/download/train.csv'
    test_url = 'https://www.kaggle.com/c/3136/download/test.csv'
    
    # extract data
    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)
    logger.info('downloaded raw trainning and test data')
    
if __name__ == '__main__':
    # getting root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # find .env automatically by walking up directories until it's found
    dotenv_path = find_dotenv()
    # load up the entries as evvironmrnt variables
    load_dotenv(dotenv_path)
    
    # call the main
    main(project_dir)

            