import logging
import simple_app

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='./DevOps/logging/myapp.log', 
                        level=logging.INFO, 
                        format='%(asctime)s [%(levelname)s] %(name)s: %(lineno)d - %(message)s',
                        filemode='w')
    logger.info('Started')
    simple_app.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()