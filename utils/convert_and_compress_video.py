from moviepy.editor import VideoFileClip
import threading
import os

def convert_and_downscale(input_path, output_path, new_width):
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Get the original width and height
    original_height, original_width = video_clip.size
    scale_ratio = original_width / original_height

    # Downscale the video clip
    new_height = int(new_width / scale_ratio)
    video_clip_resized = video_clip.resize(newsize=(new_width, new_height))

    # Write the resized video to a new file in MP4 format
    video_clip_resized.write_videofile(output_path, codec="libx264", audio_codec="aac")
    os.remove(input_path)

def process_video_in_thread(input_file, output_file, new_width):
    print('Start thread')
    thread = threading.Thread(target=convert_and_downscale, args=(input_file, output_file, new_width))
    thread.start()

if __name__ == "__main__":
    #input_file_1 = '/Users/giakhang/Downloads/RPReplay_Final1703517412.MP4'
    #output_file_1 = "/Users/giakhang/dev/LeetCode/linked_list/find_the_duplicate_number/proof_starting_point_and_metting_point_meet_at_duplicate.mp4"
    #new_width = 640

    #process_video_in_thread(input_file_1, output_file_1, new_width)

    input_file_2 = '/Users/giakhang/Downloads/RPReplay_Final1707979908.mp4'
    output_file_2 = '/Users/giakhang/dev/LeetCode/tree/construct_binary_tree_from_preorder_and_inorder_traversal/vd_construct_bt_from_pre_and_in_traversal.mp4'
    new_width = 640

    process_video_in_thread(input_file_2, output_file_2, new_width)
