
from eval_methods.eval_bert_score import *
from utils.openai_utils import *

def run_test_method(df, TestType) -> dict:
    
    if TestType == "bert text comparison":
        metrics = run_bert_score_evaluation(df, answer_1_column_name = "df_answer",
                                  answer_2_column_name = "llm_answer",
                                  similarity_threshold = 0.2)
        return metrics


