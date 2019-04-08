
import config
from  models import *
import json
con = config.Config()
con.set_in_path("./benchmarks/WN18/")
con.set_work_threads(8)
con.set_train_times(1500)
con.set_nbatches(10)	
con.set_alpha(0.1)
con.set_bern(0)
con.set_dimension(250) # or use dim=300 and train times 2000 
con.set_lmbda(0.05)
con.set_lmbda_two(0.05)
con.set_margin(1.0)
con.set_ent_neg_rate(10)
con.set_rel_neg_rate(0)
con.set_opt_method("adagrad")
con.set_save_steps(500)
con.set_valid_steps(500)
con.set_early_stopping_patience(10)
con.set_checkpoint_dir("./checkpoint")
con.set_result_dir("./result")
con.set_test_link(True)
con.set_test_triple(True)
con.init()
con.set_train_model(QuatE)
con.train()