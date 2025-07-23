import streamlit as st  
from pathlib import Path  
import google.generativeai as genai  

from api_key import api_key

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

system_prompt = """
Medical Image Analysis Role

As an expert in medical image analysis, you play a critical role in examining diagnostic images for a prestigious hospital. Your specialized knowledge enables you to identify anomalies, diseases, and health conditions within these imaging modalities, ultimately contributing to patient management and care.

Primary Responsibilities

1. Detailed Image Analysis
- Objective: Conduct thorough examinations of each medical image.
- Activities:
    - Utilize advanced imaging techniques to identify deviations from anatomical norms.
    - Focus on detecting subtle signs, irregularities, and areas of concern, including but not limited to:
        - Tumors or lesions
        - Fractures or structural abnormalities
        - Inflammation or other disease markers

2. Findings Documentation
- Objective: Systematically record your observations for clarity and utility.
- Activities:
    - Create structured reports that summarize findings.
    - Clearly articulate abnormalities or potential indications of specific diseases using standardized terminology.
    - Include visual aids or annotations if necessary to enhance understanding.

3. Recommendations and Next Steps
- Objective: Propose actionable follow-up based on analytical insights.
- Activities:
    - Suggest additional tests (e.g., MRI, CT scans, biopsies) as required.
    - Recommend consultations with specialists such as oncologists or orthopedic surgeons.
    - Outline potential treatment pathways, considering the patient's medical history and current conditions.

4. Preliminary Treatment Suggestions
- Objective: Provide initial recommendations for patient management.
- Activities:
    - If applicable, propose therapeutic options or interventions.
    - Discuss lifestyle changes, medication, or surgical options based on findings.
    - Ensure that suggestions align with current medical guidelines and protocols.

Important Considerations

1. Clinical Scope
- Respond only when presented with medical images related to human health, ensuring relevance and appropriateness of analysis.

2. Image Quality
- Acknowledge and note instances where image quality may hinder precise analysis.
- Clearly state any limitations imposed by unclear visuals to ensure transparency in evaluation.

3. Legal and Ethical Disclaimer
- Always accompany your insights with a disclaimer emphasizing the necessity of consulting a qualified physician before any clinical decisions are made based on your analysis.
- Remind relevant stakeholders about the legal implications of relying solely on AI-generated insights for medical decisions.

4. Clinical Impact Awareness
- Recognize that assessments significantly influence clinical decisions and patient outcomes.
- Approach every task with utmost diligence, accuracy, and empathy, understanding the responsibility you hold in patient care.

and please provide me an output response with these 10 headings Detailed Analysis , Findings Report , Recommendations and Next Steps, Preliminary Treatment Suggestions, Clinical Scope, Legal and Ethical Disclaimer, Clinical Impact Awareness, Estimated Treatment cost, Estimated Recovery Time,Aurvedic remidies, Home Remideis, and Conclusion.

Conclusion

Your expertise is vital in enhancing patient care. Maintain professionalism and compassion throughout your work, and ensure your analyses are grounded in the latest scientific and clinical evidence.
"""


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)

# 1. Improved Page Configuration  
st.set_page_config(  
    page_title="VitalImage Analytics",  
    page_icon=":brain:",  
    layout="wide",  
)  

# 2. Enhanced CSS Styling for the Layout, Button, and Logo Centering  
st.markdown(  
    """  
    <style>  
    body {  
        background-color: #f4f4f9;  
        font-family: 'Arial', sans-serif;  
    }  

    .main-container {  
        padding: 40px;  
        border-radius: 10px;  
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);  
        max-width: 800px;  
        margin: auto;  
        margin-top: 40px;  
        /* Removed background color to avoid the white box effect */  
        animation: fadeIn 0.5s; /* Fade in animation for container */  
    }  

    @keyframes fadeIn {  
        from { opacity: 0; }  
        to { opacity: 1; }  
    }  

    .stButton button {   
        background-color: #007bff;   
        color: white;  
        border: none;  
        padding: 15px 30px;  
        border-radius: 5px;  
        font-size: 1.2em;  
        cursor: pointer;  
        transition: background-color 0.3s, transform 0.3s;  
    }  

    .stButton button:hover {  
        background-color: #0056b3;   
        transform: scale(1.05); /* Slightly enlarge button on hover */  
    }  

    h1 {  
        color: #007bff;   
        font-size: 2.5em;  
        text-align: center;  
        margin: 20px 0;  
    }  
    
    h2 {  
        text-align: center;  
        color: #555;  
        margin-bottom: 30px;  
    }  
    
    .uploader {  
        border: 2px dashed #007bff;  
        border-radius: 10px;   
        padding: 20px;  
        text-align: center;  
        margin: 20px 0;  
        transition: background-color 0.3s;  
    }  

    .uploader:hover {  
        background-color: #f0f8ff;  
    }  

    .description {  
        color: #777;  
        margin: 10px;  
        text-align: center;  
        font-size: 1.1em;  
    }  

    .footer {  
        margin-top: 40px;  
        font-size: 0.9em;  
        text-align: center;  
    }  

    </style>  
    """,  
    unsafe_allow_html=True,  
)  

# 4. Main Content within a Styled Container  
with st.container():  
    st.markdown('<div class="main-container">', unsafe_allow_html=True)  

    # 5. Title and Subheader  
    st.markdown("<h1>VitalImage Analytics</h1>", unsafe_allow_html=True)  
    st.markdown("<h2>AI-Powered Medical Image Analysis</h2>", unsafe_allow_html=True)  

    st.markdown("<p class='description'>Upload your medical images for a comprehensive analysis powered by Gemini AI technology.</p>", unsafe_allow_html=True)  

    uploaded_file = st.file_uploader(  
        "Upload a medical image (JPG, JPEG, or PNG)",  
        type=["jpg", "jpeg", "png"],  
        label_visibility="collapsed",  
        key="file_uploader"  
    )  

    # Uploader with styling  
    st.markdown('<div class="uploader">', unsafe_allow_html=True)  
    st.markdown("Drag and drop or click here to select a file.", unsafe_allow_html=True)  
    st.markdown('</div>', unsafe_allow_html=True)  

    submit_button = st.button("Analyze Image", type="primary")  

    if submit_button:  

        image_data=uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": "image/jpeg",
                "data": image_data
            },
        ]

        prompt_parts = [

            image_parts[0],
            system_prompt,
        ]

        st.image(image_data, caption="Uploaded Image", use_column_width=True)

        response = model.generate_content(prompt_parts)
        if response:
            st.title("Here is the Medical Image Analysis Based on Your image")
            st.write(response.text)

    st.markdown('<div class="footer">© 2024 VitalImage Analytics. 404Hacks.</div>', unsafe_allow_html=True)  
    st.markdown('</div>', unsafe_allow_html=True)