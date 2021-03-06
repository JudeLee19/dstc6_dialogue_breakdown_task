import os
from general_utils import get_logger


class Config():
    def __init__(self):
        # directory for training outputs
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        self.logger = get_logger(self.log_path)
        
    # output_path = 'results/word2vec_lstm_v5/'
    # model_output = output_path + 'model.weights_v5/'
    # log_path = output_path + "log_v4.txt"
     
    output_path = 'results/word2vec_cnn_v4/'
    model_output = output_path + 'model.weights/'
    log_path = output_path + "log.txt"
    
    lr = 0.001
    lr_decay = 0.9
    clip = -1
    nepoch_no_imprv = 3
    reload = True
    
    num_epochs = 30
    batch_size = 10
    
    # embed_method = 'word2vec'
    embed_method = 'cnn'
    
    train = False
    
    # file name lists for training
    word2vec_filename = 'dbdc3/data/word2vec/wiki_en_model'
    
    train_filename = 'dbdc3/data/train_test_dir/train_dataset'
    dev_filename = 'dbdc3/data/train_test_dir/dev_dataset'
    test_filename = 'dbdc3/data/train_test_dir/test_dataset'
    