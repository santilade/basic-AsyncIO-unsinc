# AsyncIO-unsinc-basic-application
Testing [unsinc library](https://github.com/alex-sherman/unsync) that unifies **AsyncIO**, **threading** and **multiprocessing**, making it very easy to integrate all three on the same application.

- **v1.py** runs all the functions single-threaded.
- **v2-async.py** treats all the functions as asynchronous tasks even if they are not async compatible.
- **v3-unsync.py** runs async functions in the `unsync.loop` event loop, regular functions in the ThreadPoolExecutor `unsync.thread_executor` and regular functions marked with `@unsync(cpu_bound=True)` in the ProcessPoolExecutor `unsync.process_executor`
