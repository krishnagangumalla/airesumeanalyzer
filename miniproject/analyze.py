def analyzer(job_des, res_skil):
    job_des=set(job_des.lower().split())
    res_skil=set(res_skil.lower().split())
    stren=job_des & res_skil
    impro=job_des - res_skil
    res=f"""
    "strengths:" {",".join(stren) if stren else None}\n
    "improvements: "{",".join(impro) if impro else None} """
    return res
