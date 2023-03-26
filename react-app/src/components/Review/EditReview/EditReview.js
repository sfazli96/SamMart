import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { readAllReviews, editReview } from "../../../store/reviews";
import ReactStars from "react-rating-stars-component";
import { addReviews } from "../../../store/reviews";


const EditReview = ({ reviewData, onClose}) => {
    const dispatch = useDispatch()
    const reviewId = useParams()
    console.log('reviewId', reviewId)
    const [rating, setRating] = useState(5)
    const [review, setReview] = useState()
    // const [showForm, setShowForm] = useState(false)
    // const [newReviewData, setNewReviewData] = useState({});
    // const [isEdit, setIsEdit] = useState(null)
    // const [newReview, setNewReview] = useState("")
    // const [newRating, setNewRating] = useState("")
    const [errors, setErrors] = useState([])
    // const [validationErrors, setValidationErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault()
        setErrors([])
        if (!review || review.length < 3) {
            setErrors(["Please enter a review with at least 3 characters"])
            setTimeout(() => {
                setErrors([])
            }, 2000)
            return
        }
        dispatch(editReview(reviewData.id, {review, rating}))
        .then(() => {
            onClose()
        })
    }

    const handleChange = (e) => {
        if (e.target.value.length <= 200) {
            setReview(e.target.value)
        }
    }

    const ratingChanged = (newRating) => {
        setRating(newRating)
    }

    return (
        <div>
            <form onSubmit={handleSubmit} noValidate>
                    <div className="edit-review-form">
                    {errors.map((error, index) => (
                    <div key={index} className="error-msg">{error}</div>
                    ))}
                    <h2>Edit Review</h2>
                    <textarea
                    type="textbox"
                    defaultValue="Edit your amazing review here!"
                    value={review}
                    onChange={handleChange}
                    required
                    ></textarea>
                    <ReactStars
                            count={5}
                            value={rating}
                            onChange={ratingChanged}
                            size={24}
                            isHalf={true}
                            emptyIcon={<i className="far fa-star"></i>}
                            halfIcon={<i className="fa fa-star-half-alt"></i>}
                            fullIcon={<i className="fa fa-star"></i>}
                            activeColor="#ffd700"
                            />
                    <button className="submit-button" type="submit">Submit</button>
                    <button onClick={onClose}>Cancel</button>
                </div>
            </form>
        </div>
    )

}



export default EditReview