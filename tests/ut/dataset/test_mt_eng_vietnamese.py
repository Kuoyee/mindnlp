# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
Test Ptb_text_only
"""
import os
import unittest
import pytest
import mindspore as ms
from mindspore.dataset import text
from mindnlp.transforms import BasicTokenizer
from mindnlp.dataset import Hf_mt_eng_vietnamese,Hf_mt_eng_vietnamese_Process
from mindnlp import load_dataset, process


class TestMtEngVietnamese(unittest.TestCase):
    r"""
    Test mt_eng_vietnamese
    """

    @classmethod
    def setUpClass(cls):
        cls.root = os.path.join(os.path.expanduser("~"), ".mindnlp")


    @pytest.mark.download
    def test_mt_eng_vietnamese(self):
        """Test mt_eng_vietnamese"""
        num_lines = {
            "train": 133318,
            "validation": 1269,
            "test": 1269,
        }
        dataset_train, dataset_dev, dataset_test = Hf_mt_eng_vietnamese(
            root=self.root, split=("train", "validation", "test")
        )
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_dev.get_dataset_size() == num_lines["validation"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

        dataset_train = Hf_mt_eng_vietnamese(root=self.root, split="train")
        dataset_dev = Hf_mt_eng_vietnamese(root=self.root, split="validation")
        dataset_test = Hf_mt_eng_vietnamese(root=self.root, split="test")
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_dev.get_dataset_size() == num_lines["validation"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

    @pytest.mark.download
    def test_mt_eng_vietnamese_by_register(self):
        """test mt_eng_vietnamese by register"""
        _ = load_dataset(
            "Hf_mt_eng_vietnamese",
            root=self.root,
            split=("train", "validation", "test"),
        )
    
    
    @pytest.mark.download
    def test_mt_eng_vietnamese_process(self):
        r"""
        Test HF_mt_eng_vietnamese_Process
        """

        train_dataset, _, _ = Hf_mt_eng_vietnamese()
        train_dataset, vocab = Hf_mt_eng_vietnamese_Process(train_dataset)
        train_dataset = train_dataset.create_tuple_iterator()

        for _, value in vocab.vocab().items():
            assert isinstance(value, int)
            break

    @pytest.mark.download
    def test_ptb_text_only_process_by_register(self):
        """test ptb_text_only process by register"""
        train_dataset, _, _ = Hf_mt_eng_vietnamese()
        train_dataset, vocab = process('Hf_mt_eng_vietnamese',
                                       dataset=train_dataset,
                                       column="en",
                                       tokenizer=BasicTokenizer(),
                                       vocab=None
                                       )
        train_dataset = train_dataset.create_tuple_iterator()

        for _, value in vocab.vocab().items():
            assert isinstance(value, int)
            break
