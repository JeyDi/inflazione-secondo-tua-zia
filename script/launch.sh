export PYTHONPATH=$(pwd)
streamlit run app/src/streamlit/home.py --server.fileWatcherType none --server.port 8000 --browser.gatherUsageStats false --logger.level info
#python3 app/main.py