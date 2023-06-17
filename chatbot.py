import streamlit as st
from llama_index import LLMPredictor, PromptHelper, ServiceContext, VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os
import openai
from langchain.chat_models import ChatOpenAI
import asyncio

def chat_bot(request):
    #Selects the Model and sets the Temperature between 0 and 1. A higher temperature means more creative responses.
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=512))

    #Sets the chunk size limit and its overlap. You might need to play with Overlap for your data to get the best results.
    prompt_helper = PromptHelper(4096, 512, chunk_size_limit=600, chunk_overlap_ratio=0.7)

    service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    #loads from the storage folder
    storage_context = StorageContext.from_defaults(persist_dir='storage')
    
    index = load_index_from_storage(storage_context=storage_context, service_context=service_context)
    chat_engine = index.as_chat_engine()
    response = chat_engine.chat(request)

    print(response)
    return str(response)

    
