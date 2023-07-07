# In this case only INFO messages will be sent to the Report Portal.
import os
import psutil
import pytest

@pytest.mark.rp
def test_one(rp_logger):
    rp_logger.info("Case1. Step1")
    x = "this"
    rp_logger.info("x is: %s", x)
    assert 'h' in x

    # Message with an attachment.
    free_memory = psutil.cpu_percent(4)
    file =  os.path.basename("attachment.txt")

    rp_logger.info(
        "Case1. Memory consumption",
        attachment={
            "name": file,
            "data": free_memory,
            "mime": "application/octet-stream",
        },
    )

    # This debug message will not be sent to the Report Portal.
    rp_logger.debug("Case1. Debug message")
